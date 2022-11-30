use std::cmp;

fn main() {
    let base_state = GameState::new(50, 500, 71, 10);

    for (a,b) in GameState::results(base_state, 0) {
        println!("{a:?}");
    }
}

#[derive(Eq,PartialEq,Hash,Clone,Debug)]
struct GameState {
    player_life: usize,
    player_mana: usize,
    
    shield_remaining: usize,
    poison_remaining: usize,
    recharge_remaining: usize,

    enemy_life: usize,
    enemy_attack: usize
}


enum Moves {
    MagicMissile,
    Drain,
    Shield,
    Poison,
    Recharge,
    //EnemyAtk
}

#[derive(PartialEq)]
enum Outcome {
    Running,
    Win,
    Loss
}

impl GameState {

    const SHIELD_TURNS: usize = 6;
    const POISON_TURNS: usize = 6;
    const RECHARGE_TURNS: usize = 5;

    const MAG_MISS_ATK: usize = 4;
    const DRAIN_AMOUNT: usize = 2;
    const SHIELD_AMOUNT: usize = 7;
    const POISON_DMG: usize = 3;
    const RECHARGE_AMOUNT: usize = 101;

    pub fn new(life:usize, mana:usize, en_life:usize, en_atk:usize) -> GameState {
        GameState {
            player_life: life,
            player_mana: mana,

            shield_remaining: 0,
            poison_remaining: 0,
            recharge_remaining: 0,

            enemy_life: en_life,
            enemy_attack: en_atk
        }
    }

    pub fn possible_moves(&self) -> Vec<Moves> {
        let mut ans = Vec::new();

        // Game lost, no possible evolution of the state
        if self.outcome() == Outcome::Loss { return ans; }

        if self.shield_remaining <= 0 { ans.push(Moves::Shield); }
        if self.poison_remaining <= 0 { ans.push(Moves::Poison); }
        if self.recharge_remaining <= 0 { ans.push(Moves::Recharge); }

        ans.push(Moves::MagicMissile);
        ans.push(Moves::Drain);

        ans
    }

    pub fn result_of_move(&self,mov: &Moves) -> GameState {

        let mut state_copy = self.clone();

        // /////////////////////////////
        if state_copy.poison_remaining > 0 {
            state_copy.enemy_life -= GameState::POISON_DMG;
            state_copy.poison_remaining -= 1;
        }
        if state_copy.recharge_remaining > 0 {
            state_copy.player_mana += GameState::RECHARGE_AMOUNT;
            state_copy.recharge_remaining -= 1;
        }
        if state_copy.shield_remaining > 0 { state_copy.shield_remaining -= 1; }
        if state_copy.enemy_life <= 0 { return state_copy; } // Enemy dead
        // Enemy attack
        let mut shield = 0;
        if state_copy.shield_remaining > 0 { shield = GameState::SHIELD_AMOUNT; }
        state_copy.player_life -= state_copy.enemy_attack - shield;
        if state_copy.player_life <= 0 { return state_copy; } // Player dead
        // //////////////////////////////////

        // //////////////////////////////////
        if state_copy.poison_remaining > 0 {
            state_copy.enemy_life -= GameState::POISON_DMG;
            state_copy.poison_remaining -= 1;
        }
        if state_copy.recharge_remaining > 0 {
            state_copy.player_mana += GameState::RECHARGE_AMOUNT;
            state_copy.recharge_remaining -= 1;
        }
        if state_copy.shield_remaining > 0 { state_copy.shield_remaining -= 1; }
        match *mov {
            /*Moves::EnemyAtk => { 
                state_copy.enemy_life -= state_copy.enemy_attack 
            },*/
            Moves::MagicMissile => { 
                state_copy.enemy_life -= GameState::MAG_MISS_ATK 
            },
            Moves::Drain => {
                state_copy.enemy_life -= GameState::DRAIN_AMOUNT;
                state_copy.player_life -= GameState::DRAIN_AMOUNT;
            },
            Moves::Shield => {
                state_copy.shield_remaining = GameState::SHIELD_TURNS;
            },
            Moves::Poison => {
                state_copy.poison_remaining = GameState::POISON_TURNS;
            },
            Moves::Recharge => {
                state_copy.poison_remaining = GameState::RECHARGE_TURNS;
            }
        }
        // /////////////////////////////

        state_copy
    }

    pub fn outcome(&self) -> Outcome {
        if self.player_life <= 0 || self.player_mana <= 0 { Outcome::Loss }
        else if self.enemy_life <= 0 { Outcome::Win }
        else { Outcome::Running }
    }

    pub fn cost(m:&Moves) -> usize {
        match m {
            //Moves::EnemyAtk => 0,
            Moves::MagicMissile => 53,
            Moves::Drain => 73,
            Moves::Shield => 113,
            Moves::Poison => 173,
            Moves::Recharge => 229,
        }
    }

    pub fn results(state:GameState,current_cost:usize) -> Vec<(GameState,usize)> {
        let mut ans = Vec::new();

        let moves = state.possible_moves();
        for m in moves {
            let result = state.result_of_move(&m);
            //println!("{result:?}");
            //if result.outcome() != Outcome::Loss 
            {
                ans.push(
                    (
                        state.result_of_move(&m),
                        current_cost+GameState::cost(&m)
                    )
                );
            }
        }

        ans
    }
}