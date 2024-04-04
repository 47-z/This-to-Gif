from tkinter import *
from tkinter import Label as Lbl
from tkinter.filedialog import *
from tkinter.ttk import *

from PIL import Image as IMG
from urllib.request import urlopen



def main():
    # Create the main window
    root = Tk()
    root.title("Convert to GIF")
    root.geometry("500x150")

    # Create a label that will be used to show success or fail.
    status_label = Lbl(root, text="", fg="black")
    status_label.pack(pady=(5,0))

    # Create a label for instructions
    urlLabel = Label(root, text="Enter URL:")
    urlLabel.pack(pady=(10,0))

    # Create an entry widget for URL input
    url_entry = Entry(root)
    url_entry.pack(fill='x', padx=30)

    

    # Function that converts the file into a GIF
    def ConvertFile():
        try:
            # Gets the image from the url
            url = url_entry.get()
            img = IMG.open(urlopen(url))
            img.info.pop("background", None)

            # Asks user for folder and filename
            file_name = asksaveasfilename(defaultextension=".gif", initialfile="converted_output")

            if file_name:
                output_path = file_name

                try:
                    # Save image to file
                    img.save(output_path, "gif", save_all=True)
                    img.close()

                    # Resets the entry box and displays a success status
                    status_label.configure(text=f"GIF saved successfully :)", fg="green")
                    url_entry.delete(0, END)

                except IOError as e:
                    status_label.configure(text=f"Error saving file: {e}", fg="red")

        except Exception as e:
            status_label.configure(text=f"Error downloading or processing image: {e}", fg="red")



    # Create a submit button
    submit_button = Button(root, text="Convert to GIF", command=ConvertFile)
    submit_button.pack(pady=10)

    # Run the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()