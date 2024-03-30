import cv2
import streamlit as st

# Create a Streamlit app
st.title("Webcam Feed")

# Create a VideoCapture object
cap = cv2.VideoCapture(0)

# Loop over the frames from the webcam
while True:
    # Capture a frame
    ret, frame = cap.read()

    # Display the frame
    st.image(frame, caption="Webcam Feed")

    # If the user presses the 'q' key, break out of the loop
    if cv2.waitKey(1) == ord('q'):
        break

# Destroy all windows
cv2.destroyAllWindows()

'''
import streamlit as st
import cv2

def main():
    st.set_page_config(page_title="Streamlit WebCam App")
    st.title("Webcam Display Steamlit App")
    st.caption("Powered by OpenCV, Streamlit")
    cap = cv2.VideoCapture(0)
    frame_placeholder = st.empty()
    stop_button_pressed = st.button("Stop")
    while cap.isOpened() and not stop_button_pressed:
        ret, frame = cap.read()
        if not ret:
            st.write("Video Capture Ended")
            break
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_placeholder.image(frame,channels="RGB")
        if cv2.waitKey(1) & 0xFF == ord("q") or stop_button_pressed:
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
'''
