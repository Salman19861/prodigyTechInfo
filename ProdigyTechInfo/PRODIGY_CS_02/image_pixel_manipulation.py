#Image Enctyption and Decryption Using pixel manupulation
from PIL import Image
def encrypt_image(image_path, key):
    img = Image.open(image_path)
    width, height = img.size
    encrypted_pixels = []

    for y in range(height):
        for x in range(width):
            '''
            pixel: is a tuple containing the RGB values of the current pixel.
            key: is an integer value used for encryption.
            (p ^ key): performs an XOR operation between each color channel p of the pixel and the key.
            The result of the XOR operation is converted back to a tuple using tuple(),
            forming the encrypted pixel.
            '''
            
            pixel = img.getpixel((x, y))
            # Apply simple encryption operation, i.e XOR with key
            encrypted_pixel = tuple((p ^ key) for p in pixel) 
            encrypted_pixels.append(encrypted_pixel)

    encrypted_img = Image.new(img.mode, img.size)
    encrypted_img.putdata(encrypted_pixels)
    encrypted_img.save("encrypted_image.png")

def decrypt_image(image_path, key):
    img = Image.open(image_path)
    width, height = img.size
    decrypted_pixels = []

    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))
            # Apply the reverse operation for decryption
            decrypted_pixel = tuple((p ^ key) for p in pixel) #Applies the reverse operation of XOR with
            #the key to each color channel p of the pixel. 
            #This effectively cancels out the encryption operation, restoring the original pixel value.
            
            decrypted_pixels.append(decrypted_pixel)

    decrypted_img = Image.new(img.mode, img.size)
    decrypted_img.putdata(decrypted_pixels)
    decrypted_img.save("decrypted_image.png")

# Example usage:
image_path = "image.jpg"
key = 183  # You can choose any integer key, same key will be used to decrypt back the image

# Encrypt the image
# encrypt_image(image_path, key)

# Decrypt the image
decrypt_image("encrypted_image.png", key)
