from PIL import Image

def process_image(input_path, output_path, mode):
    with Image.open(input_path) as img:
        width, height = img.size
        
        for x in range(width):
            for y in range(height):
                r, g, b = img.getpixel((x, y))
                
                # Swap red and blue channels
                new_pixel = (b, g, r)
                
                img.putpixel((x, y), new_pixel)
        
        img.save(output_path)
    
    print(f"Image {mode}d successfully!")

# Image paths
input_image = r"C:\Users\Jil Patel\OneDrive\Desktop\vs code\dsa\cyber_security\input.jpg"
encrypted_image = r"C:\Users\Jil Patel\OneDrive\Desktop\vs code\dsa\cyber_security\encrypted.jpg"
decrypted_image = r"C:\Users\Jil Patel\OneDrive\Desktop\vs code\dsa\cyber_security\decrypted.jpg"

# Encrypt the image
process_image(input_image, encrypted_image, "encrypt")

# Decrypt the image
process_image(encrypted_image, decrypted_image, "decrypt")