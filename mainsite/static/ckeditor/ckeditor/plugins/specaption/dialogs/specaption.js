CKEDITOR.dialog.add( 'captionDialog', function( editor ) {
    return {
        title: 'SPE Caption Properties',
        minWidth: 400,
        minHeight: 200,
        contents: [
            {
                id: 'tab-basic',
                label: 'Basic Settings',
                elements: [
                    {
                        type: 'text',
                        id: 'caption',
                        label: 'Caption',
                        validate: CKEDITOR.dialog.validate.notEmpty( "Caption field cannot be empty." )
                        // NOTE: since this value is stored in a different element we have to do it on show and ok
                        // setup: function( element ) {
                        //     this.setValue(element.specaption);
                        // },
                        // commit: function( element ) {
                        //     element.specaption = this.getValue();
                        // }
                    },
                    {
                        type: 'select',
                        id: 'position',
                        label: 'Position',
						items: [
							[ 'Top', 'true' ],
							[ 'Bottom', 'false' ]
						],
						'default': 'true',
						onChange: function(api) {
							console.log('select changed to: ' + this.getValue());
						},
                        setup: function(element) {
                            console.log('position in element: ' + element.getAttribute('position'));
                            if (element.getAttribute('position'))
                                this.setValue(element.getAttribute('position'));
                        },
                        commit: function(element) {
                            element.setAttribute('position', this.getValue());
                        }
                    }
                ]
            },
            {
                id: 'tab-adv',
                label: 'Advanced Settings',
                elements: [
                    {
					type: 'vbox',
					padding: 1,
					children: [{
                        type: 'hbox',
                        widths: ['50%', '50%'],
                        children: [
                            {
                                type: 'text',
                                id: 'id',
                                label: 'Id',
                                'default': '',
                                setup: function(element) {
                                    this.setValue(element.getAttribute('id'));
                                },
                                commit: function(element) {
                                    element.setAttribute('id', this.getValue());
                                }
                            },
                            {
                                type: 'text',
                                id: 'name',
                                label: 'Name',
                                'default': '',
                                setup: function(element) {
                                    this.setValue(element.getAttribute('name'));
                                },
                                commit: function(element) {
                                    element.setAttribute('name', this.getValue());
                                }
                            }]
                        }]
                    },
                    {
					type: 'vbox',
					padding: 1,
					children: [{
						id: 'class',
						type: 'text',
						label: 'Class Attribute',
						'default': '',
                        setup: function(element) {
                            this.setValue(element.getAttribute('class'));
                        },
                        commit: function(element) {
                            element.setAttribute('class', this.getValue());
                        }
						}]
					},
                    {
					type: 'vbox',
					padding: 1,
					children: [{
						id: 'style',
						type: 'text',
						label: 'Style Attribute',
						'default': 'border-style: none; background-color: white;',
                        setup: function(element) {
                            this.setValue(element.getAttribute('style'));
                        },
                        commit: function(element) {
                            element.setAttribute('style', this.getValue());
                        }
						}]
					},
                    {
					type: 'vbox',
					padding: 1,
					children: [{
						id: 'tooltip',
						type: 'text',
						label: 'Tooltip Text',
						'default': '',
                        setup: function(element) {
                            this.setValue(element.getAttribute('title'));
                        },
                        commit: function(element) {
                            element.setAttribute('title', this.getValue());
                        }
						}]
					}
                ]
            }
        ],
        onShow: function() {
            var selection = editor.getSelection();
            var element = selection.getStartElement();
            var caption_element;

            if ( element )
                element = element.getAscendant( 'figure', true );

            if ( !element || element.getName() != 'figure' ) {
                element = editor.document.createElement( 'figure' );
                this.insertMode = true;
            }
            else {
                this.insertMode = false;
            }

            caption_element = element.findOne('figcaption');
            if (!caption_element || caption_element.getName() != 'figcaption' ) {
                this.getContentElement('tab-basic', 'caption').setValue('');
                caption_element = editor.document.createElement('figcaption');
                element.append(caption_element);
            }
            else
                this.getContentElement('tab-basic', 'caption').setValue(caption_element.getText());

            this.element = element;
            this.caption_element = caption_element;

            if ( !this.insertMode )
                this.setupContent( this.element );
        },
        onOk: function() {
            var original_selection = editor.getSelection();
            var original_element = original_selection.getStartElement();
            var cap = this.getContentElement( 'tab-basic', 'caption' ).getValue();
            console.log('caption value: ' + cap);

            this.caption_element.setText(cap);

            this.commitContent( this.element );

            console.log('position: ' + this.getContentElement( 'tab-basic', 'position' ).getValue());
            var is_top = false;
            if (this.getContentElement( 'tab-basic', 'position' ).getValue() == "true")
                is_top = true;

            if ( this.insertMode ) {
                // insert our caption at the next block element
                var block_ascendant = original_element.getAscendant( function( el ) {
                    return !!CKEDITOR.dtd.$block[ el.$.localName ];
                    }, true);
                this.element.insertBefore(block_ascendant);
                block_ascendant.move(this.element, !is_top);
            }
            else {
                // they may have changed the position so lets make sure it is right
                this.caption_element.move(this.element, is_top)
            }
        }
    };
});