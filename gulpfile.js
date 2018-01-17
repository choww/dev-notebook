var gulp = require('gulp');
var sass = require('gulp-sass');
var source = require('vinyl-source-stream');
var browserify = require('browserify');
var vueify = require('vueify');
var buffer = require('vinyl-buffer');

gulp.task('sass', function() {
  return gulp.src('assets/scss/*.scss')
             .pipe(sass())
             .pipe(gulp.dest('assets/css'))
});

gulp.task('vueify', function() {
  return browserify('./assets/vue/tags.js')
         .transform(vueify)
         .bundle()
         .pipe(source('tags.js'))
         .pipe(gulp.dest('./assets/js'))
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

