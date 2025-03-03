<template>
  <div>
    <div class="box">
      <div class="box-box">
        <input class="input" type="text"  v-model="link" placeholder="INGRESA EL LINK AQUI">
        <select id="op" name="thelist" onChange="combo(this, 'theinput')">
                  <option value="MP3">MP3</option>
                  <option value="MP4">MP4</option>
        </select>
        <button @click="EnviarLink"> Descargar </button>
    
      </div>
     
    </div>
   
  </div>
 
</template>

<script>
export default {
    name: 'homeSite',

    //MIS VARIABLES
    data(){
      return{
        link:""
      }
    },

    methods:{
      mostrar: function(){
        console.log(this.link)
      },

      EnviarLink: async function EnviarLink() {
        console.log(JSON.stringify({ link: this.link }))
        try {
        const response = await fetch("http://localhost:8000/api/download", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ link: this.link })
        });

   
  
        
        if (!response.ok) {
            console.error("Error al obtener el archivo");
            return;
        }

       

        const blob = await response.blob();

       
        if (blob.size === 0) {
            console.error("El archivo recibido está vacío.");
            return;
        }

        const url = window.URL.createObjectURL(blob);
        const a = document.createElement("a");
        a.href = url;
        a.download = "cancion.mp3";
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        window.URL.revokeObjectURL(url);

    } catch (error) {
        console.error("No se pudo descargar la canción:", error);
    }
      }
    },
}
</script>

<style scoped>
  * {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

  .input{
 
    border-radius: 10px;
    height: 35%;
    
  }
  .box{
    display: flex;
    justify-content: center;
    align-items: center;
    border: 2px solid black;
    height: 80vh;
  }
  .box-box{
    display: flex;
    justify-content: center;
    align-items: center ;
    gap: 5px;
    border: 1px solid black;
    border-radius: 15px;
    height: 20%;
    width: 30%;
    -webkit-box-shadow: 7px 43px 30px -4px rgba(0,0,0,0.1);
    -moz-box-shadow: 7px 43px 30px -4px rgba(0,0,0,0.1);
    box-shadow: 7px 43px 30px -4px rgba(0,0,0,0.1);
  }
</style>