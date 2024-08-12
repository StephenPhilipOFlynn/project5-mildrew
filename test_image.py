from src.data_management import load_pkl_file

def check_image_shape(version):
    image_shape = load_pkl_file(file_path=f"outputs/v1/image_shape.pkl")
    print("Loaded image shape:", image_shape)

if __name__ == "__main__":
    version = "v1"  # or whichever version you are working with
    check_image_shape(version)
