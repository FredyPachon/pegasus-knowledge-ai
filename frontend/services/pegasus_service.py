from src.agente import AgentePegasus


class PegasusService:
    """
    Servicio encargado de comunicarse
    con el Agente Pegasus.
    """

    def __init__(self):

        self.agente = AgentePegasus()

    def preguntar(self, pregunta: str):

        return self.agente.responder(pregunta)