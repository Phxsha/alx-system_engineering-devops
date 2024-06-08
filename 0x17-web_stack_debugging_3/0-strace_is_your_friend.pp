# 0-strace_is_your_friend.pp
# This Puppet manifest corrects the incorrect file extensions in wp-settings.php to prevent a server error.

define fix_extension($path, $incorrect_ext, $correct_ext) {
  exec { "fix_extension_in_${path}":
    command => "sed -i 's/${incorrect_ext}/${correct_ext}/g' ${path}",
    onlyif  => "grep -q ${incorrect_ext} ${path}",
  }
}

fix_extension { 'wp-settings.php':
  path          => '/var/www/html/wp-settings.php',
  incorrect_ext => 'phpp',
  correct_ext   => 'php',
}
