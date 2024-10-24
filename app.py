import tkinter as tk
from tkinter import messagebox
from openai import OpenAI
from PIL import Image, ImageTk
import requests
from io import BytesIO

# Initialize OpenAI client
client = OpenAI(api_key='')

# Initializing the main window and widgets
window = tk.Tk()
window.geometry("850x400")  # Expanded window size for image space
window.resizable(height=False, width=False)
window.title("DadJoke 3000 with DALL·E")

# Styling for widgets
window.configure(bg="#f7f7f7")
label_style = {"font": ("Helvetica", 14), "bg": "#f7f7f7", "fg": "#333"}
button_style = {"font": ("Helvetica", 12), "bg": "#ff5757", "fg": "white", "activebackground": "#ff3232"}

# Adding padding for better spacing
pad_x = 10
pad_y = 10

# Label for the title
label1 = tk.Label(text="Behold! Dad Jokes at your leisure!", **label_style)
label1.grid(columnspan=3, pady=(10, 20))

# Label for the input subject
label2 = tk.Label(text="Enter your joke subject below:", **label_style)
label2.grid(column=0, row=1, padx=pad_x, pady=(5, 5), sticky="w")

# Input field for the joke subject
subject = tk.Entry(window, font=("Helvetica", 12), width=30)
subject.grid(column=1, row=1, padx=pad_x, pady=(5, 5))

# Text widget to display jokes
joke_display = tk.Text(master=window, height=10, width=40, wrap="word", font=("Helvetica", 12))
joke_display.grid(column=0, row=3, padx=pad_x, pady=pad_y, columnspan=2)

# Add a loading label (initially hidden)
loading_label = tk.Label(window, text="Loading...", **label_style)
loading_label.grid(column=0, row=4, padx=pad_x, pady=pad_y, columnspan=2)
loading_label.grid_remove()  # Hide initially

# Placeholder image (can be dynamically updated)
img_placeholder = Image.open("placeholder_image.png")  # Replace this with your image path
img_placeholder = img_placeholder.resize((150, 150))
img_tk = ImageTk.PhotoImage(img_placeholder)

# Label to display image next to the joke display
image_label = tk.Label(window, image=img_tk, bg="#f7f7f7")
image_label.grid(column=2, row=3, padx=pad_x, pady=pad_y)

# Function to fetch dad joke using OpenAI
def dadjoke3000():
    search = str(subject.get()).strip()

    if not search:
        messagebox.showwarning("Input Error", "Please enter a joke subject!")
        return ""
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "system", "content": "Tell me a dad joke about the given topic."},
                      {"role": "user", "content": search}],
            temperature=0.6,
            max_tokens=200
        )
        
        joke = response.choices[0].message.content.strip()
        return joke if joke else f"I'm sorry, I have no jokes about {search}."
    
    except Exception as e:
        messagebox.showerror("API Error", f"Error: {str(e)}")
        return ""

# Function to generate image using DALL·E based on joke
def generate_image(prompt):
    try: 
        # Call DALL·E API with the prompt
        response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1
    )
        # Get the image URL
        # image_url = response['data'][0]['url']
        image_url = response.data[0].url

        # Fetch the image from the URL
        img_response = requests.get(image_url)
        img_data = Image.open(BytesIO(img_response.content))
        img_data = img_data.resize((200, 200))
        
        return ImageTk.PhotoImage(img_data)
    
    except Exception as e:
        messagebox.showerror("Image Error", f"Error generating image: {str(e)}")
        return img_tk  # Return the placeholder image in case of an error

# Displaying the joke and generated image in the text field
def jokedisplay():
    # Show the loading label
    loading_label.grid()  
    loading_label.update()  # Ensure it updates immediately

    joke = dadjoke3000()
    if joke:
        joke_display.config(state=tk.NORMAL)
        joke_display.delete(1.0, tk.END)
        joke_display.insert(tk.END, joke)
        joke_display.config(state=tk.DISABLED)
        
        # Generate the image from the joke
        img_prompt = f"Create an illustration for this joke: {joke}"
        new_img = generate_image(img_prompt)
        image_label.config(image=new_img)
        image_label.image = new_img  # Keep a reference to avoid garbage collection
    # Hide the loading label after the requests are done
    loading_label.grid_remove()

# Clear the input field and joke display
def clear_display():
    subject.delete(0, tk.END)
    joke_display.config(state=tk.NORMAL)
    joke_display.delete(1.0, tk.END)
    joke_display.config(state=tk.DISABLED)
    image_label.config(image=img_tk)  # Reset to placeholder image

# Button widget for getting a joke and image
button1 = tk.Button(
    text="Get my dad joke!", command=jokedisplay, **button_style
)
button1.grid(column=0, row=2, padx=pad_x, pady=pad_y, sticky="w")

# Button to clear the input and output
clear_button = tk.Button(
    text="Clear", command=clear_display, **button_style
)
clear_button.grid(column=1, row=2, padx=pad_x, pady=pad_y, sticky="e")

# Start the main loop
window.mainloop()
