/**
 * @module UseSprite
 * @origin 13872.js
 * @status mock
 * @purpose component for sprites
 * @globals ???
 */

<template><svg class="icon"><use :xlink:href="symbol" /></svg></template>
<script>
	export default { props: ['symbol'] };
</script>
