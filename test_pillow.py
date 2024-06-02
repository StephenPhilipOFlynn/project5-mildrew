try:
    from PIL import Image
    print("Pillow is installed and imported successfully.")
except ImportError as e:
    print(f"Error importing Pillow: {e}")
