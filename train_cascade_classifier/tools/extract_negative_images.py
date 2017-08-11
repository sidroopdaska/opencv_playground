import os
import cv2

negative_img_dir_path = '../negative_images/'


def extract_negative_images_camera():
    # turn on video capture and save the video frames as negative
    # images
    try:
        if not os.path.exists(negative_img_dir_path):
            os.makedirs(negative_img_dir_path)

        cap = cv2.VideoCapture(0)
        cap.set(cv2.CAP_PROP_FPS, 5)

        img_number = 896

        while True:
            ret, img = cap.read()
            cv2.imshow('img', img)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            resized_img = cv2.resize(gray, (100, 100))
            cv2.imwrite(negative_img_dir_path + str(img_number) + '.jpg', resized_img)

            img_number += 1

            k = cv2.waitKey(30) & 0xff
            if k == 27:
                break

    finally:
        cap.release()
        cv2.destroyAllWindows()


def extract_negative_images_url():
    pass


if __name__ == '__main__':
    extract_negative_images_camera()