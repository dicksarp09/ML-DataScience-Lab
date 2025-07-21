from ultralytics import YOLO

# Load model once globally
model = YOLO("quality_best.pt")

def run_detection(input_path, output_path):
    # Run detection
    results = model(input_path)

    # Save image with predictions to output_path
    results[0].save(filename=output_path)
