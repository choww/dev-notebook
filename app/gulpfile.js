var gulp = require('gulp');
var sass = require('gulp-sass');
var source = require('vinyl-source-stream');
var browserify = require('browserify');
var vueify = require('vueify');
var buffer = require('vinyl-buffer');
var stream = require('event-stream');

gulp.task('sass', function() {
  return gulp.src('assets/scss/*.scss')
             .pipe(sass())
             .pipe(gulp.dest('assets/css'))
});

gulp.task('vueify', function() {
  var fileDir = './assets/vue/';
  var files = ['tags.js', 'post.js'];
  var tasks = files.map(function(file) {
    return browserify(fileDir + file)
           .transform(vueify)
           .bundle()
           .pipe(source(file))
           .pipe(gulp.dest('./assets/js'));
  });

  return stream.merge.apply(null, tasks);
});

gulp.task('jsBundle', function() {
  return browserify('./assets/js/scripts.js')
          .bundle()
          .pipe(source('bundles.js'))
          .pipe(buffer())
          .pipe(gulp.dest('./assets/js'))
});

gulp.task('watch', function() {
  gulp.watch('assets/scss/**/*.scss', ['sass']);
  gulp.watch('assets/vue/**/*.js', ['vueify']);
  gulp.watch('assets/js/scripts.js', ['jsBundle']);
});

