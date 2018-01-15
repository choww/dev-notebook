var Vue = require('vue/dist/vue');

Vue.component('tag-form', {
  props: ['currTags'],
  data: function() {
    return { tags: this.currTags || '' }
  },
  computed: {
    processedTags: function() {
      return this.tags.split(',').map(function(tag) { return tag.trim() });
    }
  },
  methods: {
    addTag: function(event) { 
      if (event.key == ',') {
        
      }
    }
  },
  template: `
    <div class="field">
      <label for="id_categories">Tags</label>
      <div class="tags">
        <span :class="{'tag is-info': tag != ''}" v-for="tag in this.processedTags">
          {{ tag }}
        </span>
      </div>
      <div class="control">
        <input id="id_categories" name="categories" type="text" class="input" v-model="tags"></input>
      </div>
    </div>`
});

new Vue({
  el: '.post-form'
});
