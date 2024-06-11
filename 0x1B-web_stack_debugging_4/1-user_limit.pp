# Adjust file descriptor limits for the holberton user

file { '/etc/security/limits.d/holberton.conf':
  ensure  => file,
  content => "holberton hard nofile 10000\nholberton soft nofile 10000\n",
}
