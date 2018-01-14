#!/usr/bin/env python

# example radiobuttons.py

import pygtk

pygtk.require('2.0')
import gtk
from mayan_api_client import API
api = API(host='http://www.sspu-opava.cz:82', username='Dave', password='dbvjdu123')



dialog = gtk.FileChooserDialog("Open..",
                               None,
                               gtk.FILE_CHOOSER_ACTION_OPEN,
                               (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
                                gtk.STOCK_OPEN, gtk.RESPONSE_OK))
dialog.set_default_response(gtk.RESPONSE_OK)

filter = gtk.FileFilter()
filter.set_name("All files")
filter.add_pattern("*")
dialog.add_filter(filter)

filter = gtk.FileFilter()
filter.set_name("Images")
filter.add_mime_type("image/png")
filter.add_mime_type("image/jpeg")
filter.add_mime_type("image/gif")
filter.add_pattern("*.png")
filter.add_pattern("*.jpg")
filter.add_pattern("*.gif")
filter.add_pattern("*.tif")
filter.add_pattern("*.xpm")
dialog.add_filter(filter)

response = dialog.run()
if response == gtk.RESPONSE_OK:
    print dialog.get_filename(), 'selected'
elif response == gtk.RESPONSE_CANCEL:
    print 'Closed, no files selected'
dialog.destroy()


class RadioButtons:
    def callback(self, widget, data=None):
        print "%s was toggled %s" % (data, ("OFF", "ON")[widget.get_active()])

    def close_application(self, widget, event, data=None):
        gtk.main_quit()
        return False

    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)

        self.window.connect("delete_event", self.close_application)

        self.window.set_title("Typ dokumentu")
        self.window.set_border_width(0)

        box1 = gtk.VBox(False, 0)
        self.window.add(box1)
        box1.show()

        box2 = gtk.VBox(False, 10)
        box2.set_border_width(10)
        box1.pack_start(box2, True, True, 0)
        box2.show()


        buttons = []
        position = 0
        for result in api.metadata.metadata_types.get()['results']:
            button = gtk.RadioButton(buttons[position - 1] if position > 0 else None, result['name'])
            button.connect('toggled', self.callback, result['name'])
            box2.pack_start(button, True, True, 0)
            button.show()
            buttons.append(button)
            position += 1




        separator = gtk.HSeparator()
        box1.pack_start(separator, False, True, 0)
        separator.show()

        box2 = gtk.VBox(False, 10)
        box2.set_border_width(10)
        box1.pack_start(box2, False, True, 0)
        box2.show()

        button = gtk.Button("post")
        button.connect_object("clicked", self.close_application, self.window,
                              None)
        box2.pack_start(button, True, True, 0)
        button.set_flags(gtk.CAN_DEFAULT)
        button.grab_default()
        button.show()
        self.window.show()


def main():
    gtk.main()
    return 0


if __name__ == "__main__":
    RadioButtons()
    main()



class text_box:
    #Callback function, data arguments are ignored
    def hello(self, widget, entry):
        entry_text = self.entry.get_text()
        print("Entry contents: ".format(entry_text))


    def delete_event(self, widget, event, data=None):
        #Return of FALSE deletes event, True keeps it
        print("Delete even occurred")
        return False

    def submit(self, button):
        try:
            input = self.entry.get_text()
            print(float(input))
            return input
        except ValueError:
            print("This is not a number...")
            self.md = gtk.MessageDialog(None, gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_ERROR, gtk.BUTTONS_CLOSE, "This is not a number")
            self.md.set_position(gtk.WIN_POS_CENTER)
            self.md.run()
            self.md.destroy()


    def enter(self, button):
        try:
            input = self.entry.get_text()
            input = float(input)
            print(input)
            return input
        except ValueError:
            self.md = gtk.MessageDialog(None, gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_ERROR, gtk.BUTTONS_CLOSE, "This is not a number")
            self.md.run()
            self.md.destroy()
            print("This is not a number...")



    #Another Callback
    def destroy(self, widget, data=None):
        gtk.main_quit()

    def __init__(self):

        self.fix = gtk.Fixed()

        #create a new window
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_size_request(500, 500)
        self.window.set_title("Powder Application")
        self.window.set_position(gtk.WIN_POS_CENTER)
        vbox = gtk.VBox(False,0)
        self.window.add(vbox)
        vbox.show()

        #When window is given delete_event, close
        self.window.connect("delete_event", self.delete_event)

        #Connect the "destroy" event to a signal handler
        #Occurs with gtk_widget_destroy() or False in delete_event
        self.window.connect("destroy", self.destroy)

        #Sets border width of window
        self.window.set_border_width(10)

        #Creates button
        self.button = gtk.Button("Submit")
        #self.button.connect("clicked", self.hello, None)

        #Submit data in window on click
        self.button.connect_object("clicked", self.submit, self.window)


        #Make entry box
        self.entry = gtk.Entry()
        self.label = gtk.Label("Powder Density")
        vbox.pack_start(self.label, False, False, 0)
        self.label.show()
        self.entry.set_max_length(20)
        self.entry.select_region(0, len(self.entry.get_text()))
        #self.entry.connect("activate", self.hello, self.entry)
        self.entry.connect_object("activate", self.enter, self.window)
        vbox.pack_start(self.entry, False, False, 0)
        self.entry.show()

        #This packs the button and entry into the window
        #self.window.add(self.button)
        #self.window.add(self.entry)

        #hbox = gtk.HBox(False, 0)
        #vbox.add(hbox)
        #hbox.show()

        #The final step is to display this newly created widget.
        vbox.pack_start(self.button, False, False, 00)
        self.button.show()

        #And the window
        self.window.show()

    def main(self):
        #All PyGTK apps must have a gtk.main().  Control ends here
        #and waits for an event to occur
        gtk.main()
        return 0


#If the program is run, create a gui instance and show it
if __name__ == "__main__":
    hello = text_box()
    hello.main()


if __name__ == "__main__":
    EntryExample()
    main()
