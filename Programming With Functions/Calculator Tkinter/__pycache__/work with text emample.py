import tkinter as tk

def main():
    root = tk.Tk()
    root.title('Text Alignment in Tkinter')
    root.geometry('300x300')

    # Label with left-aligned text
    label_left = tk.Label(root, text='Left-aligned Label', anchor='w', width=25, bg='lightgrey')
    label_left.pack(pady=5)

    # Label with center-aligned text
    label_center = tk.Label(root, text='Center-aligned Label', width=25, bg='lightblue')
    label_center.pack(pady=5)

    # Label with right-aligned text
    label_right = tk.Label(root, text='Right-aligned Label', anchor='e', width=25, bg='lightgreen')
    label_right.pack(pady=5)

    # Entry with centered text
    entry_center = tk.Entry(root, justify='center')
    entry_center.pack(pady=5)
    entry_center.insert(0, "Centered Text Entry")

    # Text widget with justified text
    text_widget = tk.Text(root, height=4, width=25, wrap='word')
    text_widget.pack(pady=5)
    text_widget.insert('1.0', "This is a Text widget example with centered text using tags.")
    text_widget.tag_configure('center', justify='center')
    text_widget.tag_add('center', '1.0', 'end')

    root.mainloop()

if __name__ == '__main__':
    main()