CKEDITOR.plugins.add( 'specaption', {
    icons: 'specaption',
    requires: 'dialog',
    init: function( editor ) {
        console.log('spetest init...');
        if ( editor.blockless )
            return;

        // // adding a widget for the caption portion and removing from the dialog so it can contain html
        // editor.widgets.add( 'specaption', {
        //     template:   '<caption class="specaption-content">' +
        //                 '</caption>',
        //     editables: {
			// 	caption: {
			// 		selector: 'figcaption',
			// 		allowedContent: 'br em strong sub sup u s; a[!href,target]'
			// 	}
			// }
        //
        // });
        //
		//editor.addCommand('specaption', new CKEDITOR.dialogCommand('specaptionDialog'));
        editor.addCommand('specaption', new CKEDITOR.dialogCommand('captionDialog'));
        editor.addCommand( 'removespecaption', {
            exec: function( editor ) {
                var selection = editor.getSelection();
                var element = selection.getStartElement();
                var caption_element;

                if ( element )
                    element = element.getAscendant( 'figure', true );

                if ( element && element.getName() == 'figure' ) {
                    caption_element = element.findOne('figcaption');
                    if (caption_element && caption_element.getName() == 'figcaption') {
                        caption_element.remove();
                    }
                    else
                        console.log ('figure had no caption to remove!');
                    element.remove(true);
                }
                else
                    console.log('no figure found to remove!');
            }
        });

		editor.ui.addButton('SpeCaption', {
			label: 'Create Caption Container',
			command: 'specaption',
			toolbar: 'insert'
		});

        if ( editor.contextMenu ) {
            editor.addMenuGroup( 'speGroup' );
            editor.addMenuItem( 'specaptionItem', {
                label: 'Edit Caption',
                icon: this.path + 'icons/caption-blue.png',
                command: 'specaption',
                group: 'speGroup'
            });
            editor.addMenuItem( 'removespecaptionItem', {
                label: 'Remove Caption',
                icon: this.path + 'icons/caption-blue-delete.png',
                command: 'removespecaption',
                group: 'speGroup'
            });

            editor.contextMenu.addListener( function( element ) {
                if ( element.getAscendant( 'figure', true ) ) {
                    return { specaptionItem: CKEDITOR.TRISTATE_OFF,
                        removespecaptionItem: CKEDITOR.TRISTATE_OFF };
                }
            });
        }

		// tutorial example to load the dynamic portion of the ckeditor dialog framework
        CKEDITOR.dialog.add( 'captionDialog', this.path + 'dialogs/specaption.js' );

	}
});