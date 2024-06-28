from tkinter import *
import threading
import os
from diffusers import StableDiffusionPipeline
from PIL import Image, ImageTk

width = 800
height = 400
spinner_label = None
spinner_states = ["-", "\\", "|", "/"]
current_state = 0
spinner_running = False

def start_spinner():
    global spinner_running, current_state
    if spinner_running:
        spinner_label.config(text=spinner_states[current_state])
        current_state = (current_state + 1) % len(spinner_states)
        window.after(100, start_spinner)

def stop_spinner():
    global spinner_running
    spinner_running = False
    spinner_label.config(text="Chargement terminé")

def generate_image():
    def _generate():
        global spinner_running
        spinner_running = True
        start_spinner()
        
        prompt = entry.get()
        pipe = StableDiffusionPipeline.from_pretrained("hf-internal-testing/tiny-stable-diffusion-torch")
        image = pipe(prompt).images[0]
        
        if os.path.exists("generated_image.png"):
            os.remove("generated_image.png")
        image.save("generated_image.png")
        
        pil_image = Image.open("generated_image.png")
        img = ImageTk.PhotoImage(pil_image)

        # Conserver une référence à l'image pour éviter qu'elle soit effacée par le ramasse-miettes
        canvas.image = img

        # Insérer l'image dans le canvas
        canvas.create_image(width/2, height/2, image=img)
        stop_spinner()

    # Créer et démarrer un thread pour la génération de l'image
    thread = threading.Thread(target=_generate)
    thread.start()

window = Tk()
window.geometry('1080x720')
window.minsize(480, 360)
window.title('Image Generator')
window['bg'] = 'white'
window.resizable(height=True, width=True)

frame = Frame(window, bg='white')
frame.pack(expand=YES)

titre = Label(frame, text="IMAGE GENERATOR", font=("Helvetica", 25))
titre.pack(pady=15)

frame_entry = Frame(frame, bg='white')
frame_entry.pack()

label = Label(frame_entry, text="Description:", font=("Helvetica", 15), bg='white')
label.grid(row=0, column=0)

entry = Entry(frame_entry, font=("Helvetica", 15), bg="white", width=40)
entry.grid(row=0, column=2, pady=30, padx=30, ipadx=5, ipady=5)

button = Button(frame, text="Générer une Image", font=("Helvetica", 15), bg="#4065A4", fg='white', command=generate_image)
button.pack(pady=20)

spinner_label = Label(frame, text="Aucun chargement en attente", font=("Helvetica", 15), bg='white')
spinner_label.pack()

canvas = Canvas(frame, width=width, height=height, bg='black', bd=0, highlightthickness=0)
canvas.pack()

window.mainloop()
