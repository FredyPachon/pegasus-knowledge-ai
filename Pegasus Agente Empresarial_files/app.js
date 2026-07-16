// ======================================================
// PEGASUS AGENTE EMPRESARIAL
// ======================================================

const boton = document.getElementById("btnConsultar");

const pregunta = document.getElementById("pregunta");

const respuesta = document.getElementById("respuesta");

boton.addEventListener("click", async () => {

    const consulta = pregunta.value.trim();

    if (consulta === "") {

        alert("Escribe una consulta.");

        return;
    }

    respuesta.innerHTML = "🤖 Analizando documentación...";

    try {

        const request = await fetch("/preguntar", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                pregunta: consulta
            })

        });

        const data = await request.json();

        respuesta.innerHTML = data.respuesta;

    } catch (error) {

        respuesta.innerHTML = "❌ Error al conectar con Pegasus.";

        console.error(error);

    }

});