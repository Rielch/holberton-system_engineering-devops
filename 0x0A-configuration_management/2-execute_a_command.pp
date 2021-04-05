#Stop the process killmenow
exec { 'killmenow':
    path    => '/usr/bin/',
    command => 'pkill -f "killmenow"',
}
