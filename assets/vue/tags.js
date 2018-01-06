var Vue = require('vue/dist/vue');

Vue.component('post-form', {
  data: function() {
    return { tags: '' }
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
    <div>
      <div class="field">
        <label>Title</label>
        <div class="control">
          <input class="input" type="text"></input>
        </div>
      </div>

      <div class="field">
        <label>Post</label>
        <div class="control">
          <textarea class="textarea"></textarea>
        </div>
      </div>
      <div class="field">
        <label>Tags</label>
        <div class="tags">
          <span :class="{'tag is-info': tag != ''}" v-for="tag in this.processedTags">
            {{ tag }}
          </span>
        </div>
        <div class="control">
          <input type="text" class="input" v-model="tags"></input>
        </div>
      </div>
    </div>`
});

new Vue({
  el: '.post-form'
});
