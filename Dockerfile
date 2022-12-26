FROM dbswlgp99/dbswlgp99:0.0.2

COPY ./face_recogniser2.pkl /facenet/face-recognition/model/face_recogniser.pkl

WORKDIR /facenet/face-recognition

ENTRYPOINT ["python3"]

CMD ["-u","-m","inference.video_classifier"]

#CMD ["python3","hello.py";,"python3","-m","inference.video_classifier"]

#CMD ["-m","inference.video_classifier"]
