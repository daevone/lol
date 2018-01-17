import pygtk

pygtk.require('2.0')
import gtk
from mayan_api_client import API

api = API(host='http://www.sspu-opava.cz:82', username='Dave', password='dbvjdu123')
dokument = ""
metadata = ""
active_label_id = ""


class RadioButtons:
    def callback(self, widget, data=None):
        global active_label_id
        active_label_id = data
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
        for result in api.documents.document_types.get()['results']:
            button = gtk.RadioButton(buttons[position - 1] if position > 0 else None, result['label'])
            button.connect('toggled', self.callback, result['id'])
            global labels
            labels.append(result['id'])
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
    def hello(self, widget, entry):
        entry_text = self.entry.get_text()
        print("Entry contents: ".format(entry_text))

    def delete_event(self, widget, event, data=None):
        print("Delete even occurred")
        return False

    def submit(self, button):
        try:
            input = self.entry.get_text()
            print(float(input))
            return input
        except ValueError:
            print("This is not a number...")
            self.md = gtk.MessageDialog(None, gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_ERROR, gtk.BUTTONS_CLOSE,
                                        "This is not a number")
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
            self.md = gtk.MessageDialog(None, gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_ERROR, gtk.BUTTONS_CLOSE,
                                        "This is not a number")
            self.md.run()
            self.md.destroy()
            print("This is not a number...")

    def destroy(self, widget, data=None):
        gtk.main_quit()

    def __init__(self):

        self.fix = gtk.Fixed()

        # create a new window
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_size_request(300, 300)
        self.window.set_title("metadata")
        self.window.set_position(gtk.WIN_POS_CENTER)
        vbox = gtk.VBox(False, 0)
        self.window.add(vbox)
        vbox.show()

        self.window.connect("delete_event", self.delete_event)
        self.window.connect("destroy", self.destroy)
        self.window.set_border_width(10)
        self.button = gtk.Button("Submit")
        self.button.connect_object("clicked", self.submit, self.window)

        for result in api.metadata.metadata_types.get()['results']:
            self.entry = gtk.Entry()
            self.label = gtk.Label(result['name'])
            vbox.pack_start(self.label, False, False, 0)
            self.label.show()
            self.entry.set_max_length(20)
            self.entry.select_region(0, len(self.entry.get_text()))
            self.entry.connect_object("activate", self.enter, self.window)
            vbox.pack_start(self.entry, False, False, 0)
            self.entry.show()

        vbox.pack_start(self.button, False, False, 00)
        self.button.show()

        self.window.show()

    def main(self):
        gtk.main()
        return 0


if __name__ == "__main__":
    hello = text_box()
    hello.main()


    def main():
        # file filters used with the filechoosers
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
        all_filter = gtk.FileFilter()
        all_filter.set_name("All files")
        all_filter.add_pattern("*")

        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.set_title("Native Filechooser")

        window.connect("destroy", lambda wid: gtk.main_quit())
        window.connect("delete_event", lambda e1, e2: gtk.main_quit())

        button_open = gtk.FileChooserButton("Open File")
        button_open.add_filter(filter)
        button_open.add_filter(all_filter)
        button_open.connect("selection-changed", on_file_selected)

        window.add(button_open)
        window.show_all()


    print dokument


    def on_file_selected(widget):
        filename = widget.get_filename()
        print "File Choosen: ", filename
        with open(filename) as file_object:
            global active_label_id
            response = api.documents.documents.post({'document_type': active_label_id}, files={'file': file_object})


    if __name__ == "__main__":
        main()
    gtk.main()