FROM postgres:14
EXPOSE 5435

ENV POSTGRES_PASSWORD="password"

CMD ["-p", "5435"]

