# - perl -
use strict;
use warnings;
use Data::Dumper qw{Dumper};
use Test::More tests => 10;
use Date::Holidays::US qw{is_holiday};

{
my $expect = 'Day before Christmas Day';

is(is_holiday(2019,12,24), $expect);
is(is_holiday(2020,12,24), $expect);
is(is_holiday(2023,12,24), undef);
is(is_holiday(2024,12,24), $expect);
is(is_holiday(2025,12,24), $expect);
}

{
my $expect = 'Day following Christmas Day';

is(is_holiday(2013,12,26), undef);
is(is_holiday(2014,12,26), $expect);
is(is_holiday(2015,12,26), undef);
is(is_holiday(2024,12,26), undef);
is(is_holiday(2025,12,26), $expect);
}
