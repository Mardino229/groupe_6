from tkinter import *
import threading
import os
from diffusers import StableDiffusionPipeline
from diffusers.models.modeling_outputs import Transformer2DModelOutput
from PIL import Image, ImageTk
# prompt = "a photo of an astronaut riding a horse on mars"
# image = pipe(prompt).images[0]
# image.save("astronaut_rides_horse.png")
width = 800
height = 400
spinner_label = None
spinner_states = ["-", "\\", "|", "/"] 
current_state = 0

def start_spinner():
    global spinner_label
    global current_state
    # Mettre à jour le texte du label avec le prochain état du spinner
    spinner_label.config(text=spinner_states[current_state])
    # Passer à l'état suivant
    current_state = (current_state + 1) % len(spinner_states)
    # Planifier la prochaine mise à jour
    window.after(100, start_spinner)

def stop_spinner():
    global spinner_label
    if spinner_label is not None:
        spinner_label.pack_forget()

def generate_image():
    def _generate():
            start_spinner()
            prompt = entry.get()
            pipe = StableDiffusionPipeline.from_pretrained("hf-internal-testing/tiny-stable-diffusion-torch")
            image = pipe(prompt).images[0]
            if os.path.exists("generated_image.png"):
                os.remove("generated_image.png")
            image.save("generated_image.png")
            if hasattr(canvas, 'image_id'):
                canvas.delete(canvas.image_id)
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
window.minsize(480,360)
window.title('Ma première fenètre')
window['bg'] = 'white'
window.resizable(height=True, width=True)

frame = Frame(window, bg='white')
frame.pack(expand=YES)

titre = Label(frame, text="IMAGE GENERATOR", font = ("Heltevica", 25))
titre.pack(pady=15)

frame_entry = Frame(frame, bg='white')
frame_entry.pack()

label = Label(frame_entry, text="Description:", font = ("Heltevica", 15), bg='white')
label.grid(row=0, column=0)

entry = Entry(frame_entry, font = ("Heltevica", 15), bg="white", width=40)
entry.grid(row=0,column=2, pady=30, padx=30, ipadx=5,ipady=5)

button = Button(frame, text="Generate Image",font = ("Heltevica", 15), bg="#4065A4", fg='white', command=generate_image)
button.pack(pady=20)

spinner_label = Label(frame, text="Aucun chargement en attente")
spinner_label.pack()

canvas = Canvas(frame, width=width, height=height, bg='#4065A4', bd=0, highlightthickness=0)
canvas.pack()

window.mainloop()