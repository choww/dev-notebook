var Vue = require('vue/dist/vue');
var Editor = require('@tinymce/tinymce-vue');
var tags = require('./tags.js');

//Vue.component('wysiwyg-editor', {});

new Vue({
  el: '.post-form', 
  components: { 
    'editor': Editor,
    'tag-form': tags
  }
});
