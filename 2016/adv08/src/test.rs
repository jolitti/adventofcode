#[cfg(test)]

mod tests {

    use crate::screen::{Screen};

    const SAMPLE_COMMANDS: &'static [&'static str] = &[
        "rect 3x2",
        "rotate column x=1 by 1",
        "rotate row y=0 by 4",
        "rotate column x=1 by 1"
    ];

    #[test]
    fn test_check() {
        assert!(true);
    }

    #[test]
    fn keeps_pixel_number() {
        let mut sample_screen = Screen::new();
        assert_eq!(sample_screen.lit_pixels(), 0);

        for s in SAMPLE_COMMANDS {
            sample_screen.execute_str(s);
        }

        assert_eq!(sample_screen.lit_pixels(),6);
    }
}