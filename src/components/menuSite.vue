<template>
  <div>
    
            <menu class="menu">
                <div class="menu-menu">
                    <li>HOME</li>
                    <li>HOME</li>
                    <li>HOME</li>
                    <li>HOME</li>
                </div>
                <h3> DESCARGADOR</h3>
            </menu>
            
  
     
  </div>
</template>

<script>
export default {
    name: "menuSite"
}
</script>

<style scoped>
     * {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
    .menu{
        display: flex;
        flex-direction: column;
        justify-content: center;
        background-color: black;
        height: 20vh;
        gap: 10px;
    }
    .menu-menu{
        justify-content: center;
        display: flex;
        flex-direction: row;
    }
</style>