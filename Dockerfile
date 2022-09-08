FROM python:3.10.4-alpine3.15

WORKDIR /population_app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .
ENV FLASK_APP=/population_app/population_app.py
EXPOSE 5000
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000"]

# USAGE
# docker run -d --name saif1 -p:6002:5000 iqbaldocker1/population_app:v1
# curl localhost:6002/population?country=UnitedStates
# 85.6
