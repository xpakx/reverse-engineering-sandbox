/**
 * @module Game
 * @origin 97867.js
 * @status mock
 * @purpose Game shell
 * @globals ???
 */

<template>
  <div class="game-container">
    <h2>Game Canvas / Wrapper Component</h2>
    <p>Mock Component</p>
  </div>
</template>

<script>
export default {
  name: "GameContainer",
  computed: {
    isLoaded() {
      return window.is_game_loaded;
    }
  }
};
</script>

<style scoped>
.game-container {
  padding: 2rem;
  border: 2px dashed #42b883;
  text-align: center;
  margin: 2rem auto;
  max-width: 600px;
}
</style>
