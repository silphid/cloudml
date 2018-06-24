FROM frolvlad/alpine-python-machinelearning
ENV PORT 8080
EXPOSE 8080
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . /usr/src/app
ENTRYPOINT ["python"]
CMD ["app.py"]