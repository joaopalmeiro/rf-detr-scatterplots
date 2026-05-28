from rfdetr import RFDETRMedium

if __name__ == "__main__":
    model = RFDETRMedium()

    detections = model.predict("output/dataset/test/gaussian_blobs+100+2+0_2+0+x2_point_size.jpg", threshold=0.5)

    print(detections)
