var Vue = require('vue/dist/vue');
var $ = require('jquery');

var tags = Vue.component('tag-form', {
  props: ['currTags'],
  data: function() {
    return { tags: this.currTags || '' }
  },
  computed: {
    processedTags: function() {
      return this.tags.split(',').map(function(tag) { return tag.trim() });
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

var deleteBtn = Vue.component('delete-btn', {
  data: function() {
    return { clicked: false };
  },
  methods: {
    click: function() {
      this.clicked = !this.clicked; 
    }
  }
});


if ($('.post-form').length > 0) {
  new Vue({
    el: '.post-form',
    components: { 'delete-btn': deleteBtn,
      'tag-form': tags }
  });
}
