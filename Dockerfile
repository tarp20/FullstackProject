FROM node:10-alpine as frontend
WORKDIR /app
COPY frontend .
RUN npm install
RUN npm run build


FROM python:3.9-alpine
WORKDIR /apcp
COPY backend .
COPY --from=frontend /app/dist /vue
RUN pip install -r req.txt
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]