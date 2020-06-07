from pydantic import BaseModel


class Endpoint(BaseModel):
    protocol: str = "http"
    url: str
    port: int = 8080

    def compose_url(self) -> str:
        return f"{self.protocol}://{self.url}:{self.port}"
