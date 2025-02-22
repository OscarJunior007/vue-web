<template>
  <div>
    <input type="text"  v-model="link" placeholder="INGRESA EL LINK AQUI">
    <button @click="EnviarLink"> IMPRIMIR </button>
  </div>
  <h1> hola como estas</h1>
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
        try{
          let response = await fetch(`http://localhost:8000/api/obtener-link`,{
              method:"POST",
              headers:{
                'Content-Type': 'application/json'
              },
              body: JSON.stringify({ link: this.link })
            })
            console.log(this.link)
            if(!response.ok){
              console.log("La informacion no se envio correctamente")
              return
            }
            
            alert("SE ENVIO LA INFORMACION CORRECTAMENTEA")
        
        }catch(error){
              console.log(`No se pudo enviar la informacion: ${error}`)
        }
            
       
        
      }
    },
}
</script>

<style>

</style>