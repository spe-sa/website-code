/*
    script to validate urls on an admin screen or a plugin.
    Dependencies:
        This script is dependent on a webservice call that returns a json valid attribute set to "true" or "false"
        NOTE: example api code in comments below (currently checks to see if we can resolve the url)

    Usage:
        - must be based on a form
        - in the form create one or more controls with the same name as the model and pass in a data-validate-url attribute set to true
        - add this javascript to the admin screen or plugin

        Admin Ex:
        -------------
        class MyValidatorAdmin(admin.ModelAdmin):
            form=MyValidatorForm

        admin.site.register(MyValidator, MyValidatorAdmin)

        Form Ex:
        -------------
        class MyValidatorForm(ModelForm):
            myurl = forms.CharField(widget=forms.TextInput(attrs={'data-validate-url': 'true'}))

            class Meta:
                model = MyValidator
                exclude = []

            class Media:
                js=(
                    'js/validate_urls.js',
                )

        Model Ex:
        -------------
        class MyValidator(models.Model):
            myurl = models.CharField(max_length=250, null=True, blank=True)

            def __unicode__(self):
                if self.myurl:
                    return self.myurl
                else:
                    return ""

        Api View Ex:
        -------------
        @SEE: spe_api.views.UrlValidation

 */
var $ = django.jQuery;
function absolute(base, relative) {
    // make sure relative is not already absolute; we determine if it is absolute in that it has '://'.
    if (relative.indexOf('://') > -1)
        return relative;
    // make sure our base has a protocol or return the relative path
    var pos = base.indexOf('://');
    if ( pos === -1) {
        // console.log ('Warning: [' + base + '] did not detect a protocol; skipping further processing...');
        return relative;
    }
    // extract the protocol part of our base
    var protocol = base.substring(0, pos);
    // next; we could have a protocol independent url like '//maxcdn.com/stuff' so check for it and add the base in and return
    if ( relative.indexOf('//') === 0)
        return protocol + ':' + relative;
    // now we could have a relative to docroot url which should start with a single slash (double has been handled)
    if ( relative.indexOf('/') === 0) {
        // we need to determine the pos at the end of the domain but not including the /
        pos += 3;  // moves us past the :// part
        pos = base.indexOf('/', pos);
        // return the part up to the postion after the domain part and then the relative stuff (not including the trailing slash on base)
        return base.substring(0, pos) + relative;
    }
    // we will assume everything else is relative, however, django adds a trailing slash always so lets remove it if it exists
    if (base.endsWith('/'))
        base = base.substring(0, base.length-1);

    // take the current location in entirity; remove any file and extension and tack on our relative
    var stack = base.split("/"),
        parts = relative.split("/");
    stack.pop(); // remove current file name (or empty string)
                 // (omit if "base" is the current folder without trailing slash)
    for (var i=0; i<parts.length; i++) {
        if (parts[i] == ".")
            continue;
        if (parts[i] == "..")
            stack.pop();
        else
            stack.push(parts[i]);
    }
    return stack.join("/");
}

$(document).ready(function() {
    var force_submit = false;
    var data_sets = [];
    var data_set = {};
    // instead of hardcoding find all form elements which have a field with an attribute we are looking for
    // console.log("");
    $('form').each(
        function(index) {
            // console.log('[' + index + '] ' + $(this)[0].name + ': ' + $(this)[0].id);
            // $(this).submit(function( event ) {
            //     alert ("submit method worked!");
            // });
            var elcount = $(this).find('input[data-validate-url="true"]').filter(function () {
                    return !!this.value;
                    }).length;
            if ( elcount > 0) {
                // console.log('    [' + elcount + '] input elments with data-validate-url attributes found');
                $(this).on("submit", function( event ) {
                    //event.preventDefault();
                    var thisform = $(this);
                    // console.log('attached the event!');
                    data_sets = [];
                    // NOTE: changing to including in one object since params don't seem to be working with arrays
                    data_set = {};
                    // NOTE: jQuery params are not working as expected; building them myself
                    $(this).find('input[data-validate-url="true"]').filter(function () {return !!this.value;}).each(
                        function(index) {
                            // console.log('        [' + index + '] ' + $(this)[0].name + ': ' + $(this)[0].id + ' - ' + $(this)[0].value);
                            // data_set = {};
                            data_set[$(this)[0].name]=absolute(document.location.href, $(this)[0].value);
                            //data_sets.push(data_set);
                    });

                    // console.log('data_sets before ws call: ' + JSON.stringify(data_sets));
                    // console.log('data_set before ws call: ' + JSON.stringify(data_set));
                    // console.log('data_sets length:' + data_sets.length);
                    // if (data_sets.length > 0) {
                    if (! $.isEmptyObject(data_set)) {
                        var sdata = $.param(data_set);
                        // console.log(sdata); //print data in console
                        // console.log(" ");
                        if (force_submit !== true) {
                            event.preventDefault();

                            $.ajax({
                                url: "/api/validation/url/", // the endpoint
                                type: "GET", // http method
                                data: sdata, // data sent with the post request

                                // handle a successful response
                                success: function (json) {
                                    // console.log(json); // log the returned json to the console
                                    // console.log(JSON.stringify(json));
                                    // console.log("success"); // another sanity check
                                    if (json.valid !== true) {
                                        // console.log("not valid; showing alert...");
                                        var resp = confirm("You entered one or more URLs that could not be validated.  Are you sure you want to save and continue?");
                                        if (resp === true) {
                                            force_submit = true;
                                            $(thisform).submit();
                                        }
                                    }
                                    else {
                                        force_submit = true;
                                        $(thisform).submit();
                                    }
                                },

                                // handle a non-successful response
                                error: function (xhr, errmsg, err) {
                                    $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: " + errmsg +
                                        " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                                    // console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
                                    var resp = confirm("An error occured attempting to validate the URL.  See the console output for details.  Do you want to continue anyway?");
                                    if (resp === true) {
                                        force_submit = true;
                                        $(this).submit();
                                    }
                                }
                            });

                        }
                    }
                });
            }
            else {
                // console.log('    no input elements with data-validate-url attributes found');
            }
        }
    );
});
