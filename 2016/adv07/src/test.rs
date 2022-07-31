#[cfg(test)]
mod tests {

    use crate::util;

    const VALID_ADDRESSES: &'static [&'static str] = 
        &["abba[mnop]qrst", "ioxxoj[asdfgh]zxcvbn", "abba[abcd]abcd[abcd]abcd"];

    const INVALID_ADDRESSES: &'static [&'static str] = 
        &["abcd[bddb]xyyx", "aaaa[qwer]tyui"];

    const VALID_SSL: &'static [&'static str] = 
        &["aba[bab]xyz", "aaa[kek]eke","zazbz[bzb]cdb"];

    const INVALID_SSL: &'static [&'static str] = 
        &["xyx[xyx]xyx", "aaa[bbb]aaa[bbb]"];

    #[test]
    fn ip_test_pass() {
        for addr in VALID_ADDRESSES {
            assert!(util::is_valid_ipv7(addr));
        }
    }

    #[test]
    fn ip_test_fail() {
        for addr in INVALID_ADDRESSES {
            assert!(!util::is_valid_ipv7(addr));
        }
    }

    #[test]
    fn ssl_pass() {
        for addr in VALID_SSL {
            assert!(util::supports_ssl(addr));
        }
    }

    #[test]
    fn ssl_fail() {
        for addr in INVALID_SSL {
            assert!(!util::supports_ssl(addr));
        }
    }
}