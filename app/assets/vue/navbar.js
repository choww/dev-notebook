var Vue = require('vue/dist/vue');
var $ = require('jquery');

Vue.component('nav-burger', {
  data: function() { 
    return { 
      active: false 
    };
  },
  methods: {
    toggle: function() {
      this.active = !this.active;
      $('.navbar-menu').toggleClass('is-active');
    }
  }
});

new Vue({
  el: '.navbar'
});
