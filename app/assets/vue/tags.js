var Vue = require('vue/dist/vue');
var $ = require('jquery');

//Vue.component('tag-form', 
var tags = { props: ['currTags'],
  data: function() {
    return { tags: this.currTags || '' }
  },
  computed: {
    processedTags: function() {
      return this.tags.split(',').map(function(tag) { return tag.trim() });
    }
  },
}

//if ($('.post-form').length > 0) {
//  new Vue({
//    el: '.post-form'
//  });
//}
