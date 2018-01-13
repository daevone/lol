#!/usr/bin/env python

# example radiobuttons.py

import pygtk

pygtk.require('2.0')
import gtk
from mayan_api_client import API
api = API(host='http://www.sspu-opava.cz:82', username='Dave', password='dbvjdu123')
for result in api.metadata.metadata_types.get()['results']:
    jmeno=result['name']
    print(jmeno)

for result in api.documents.document_types.get()['results']:
    print(result['label'])

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

        button = gtk.RadioButton(None, "radio button1")
        button.connect("toggled", self.callback, "radio button 1")
        box2.pack_start(button, True, True, 0)
        button.show()

        button = gtk.RadioButton(button, "radio button2")
        button.connect("toggled", self.callback, "radio button 2")
        button.set_active(True)
        box2.pack_start(button, True, True, 0)
        button.show()

        button = gtk.RadioButton(button, "radio button3")
        button.connect("toggled", self.callback, "radio button 3")
        box2.pack_start(button, True, True, 0)
        button.show()

        separator = gtk.HSeparator()
        box1.pack_start(separator, False, True, 0)
        separator.show()

        box2 = gtk.VBox(False, 10)
        box2.set_border_width(10)
        box1.pack_start(box2, False, True, 0)
        box2.show()

        button = gtk.Button("close")
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


class EntryExample:
    def enter_callback(self, widget, entry):
        entry_text = entry.get_text()
        print "Entry contents: %s\n" % entry_text

    def entry_toggle_editable(self, checkbutton, entry):
        entry.set_editable(checkbutton.get_active())

    def entry_toggle_visibility(self, checkbutton, entry):
        entry.set_visibility(checkbutton.get_active())

    def __init__(self):
        # create a new window
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.set_size_request(200, 100)
        window.set_title("GTK Entry")
        window.connect("delete_event", lambda w, e: gtk.main_quit())

        vbox = gtk.VBox(False, 0)
        window.add(vbox)
        vbox.show()

        entry = gtk.Entry()
        entry.set_max_length(50)
        entry.connect("activate", self.enter_callback, entry)
        entry.set_text("hello")
        entry.insert_text(" world", len(entry.get_text()))
        entry.select_region(0, len(entry.get_text()))
        vbox.pack_start(entry, True, True, 0)
        entry.show()

        hbox = gtk.HBox(False, 0)
        vbox.add(hbox)
        hbox.show()

        check = gtk.CheckButton("Editable")
        hbox.pack_start(check, True, True, 0)
        check.connect("toggled", self.entry_toggle_editable, entry)
        check.set_active(True)
        check.show()

        check = gtk.CheckButton("Visible")
        hbox.pack_start(check, True, True, 0)
        check.connect("toggled", self.entry_toggle_visibility, entry)
        check.set_active(True)
        check.show()

        button = gtk.Button(stock=gtk.STOCK_CLOSE)
        button.connect("clicked", lambda w: gtk.main_quit())
        vbox.pack_start(button, True, True, 0)
        button.set_flags(gtk.CAN_DEFAULT)
        button.grab_default()
        button.show()
        window.show()


def main():
    gtk.main()
    return 0


if __name__ == "__main__":
    EntryExample()
    main()
