<template>
  <div>
    <h2>I'm the About Page</h2>
    <p>I'm the content.</p>
    <p>I'm the content.{{message}}</p>
  </div>
</template>

<script>
export default {
  name: 'About',
  data () {
    return {'message': 'aboutaboutaboutabout'}
  }
}
</script>