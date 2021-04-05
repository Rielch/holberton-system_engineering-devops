#Creates the file /tmp/holberton in the directory /tmp/holberton
file { '/tmp/holberton':
    path    => '/tmp/holberton',
    content => 'I love Puppet',
    group   => 'www-data',
    owner   => 'www-data',
    mode    => '0744',
}