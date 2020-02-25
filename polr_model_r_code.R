install.packages("MASS")
library(MASS)
phobia_personality_data = read.csv("Data/personality_traits.csv", header = TRUE)
View(phobia_personality_data)

model_fit <- polr(heights ~ Daily_events + Prioritising_workload + Writing_notes + Workaholism +
                    Thinking_ahead + Final_judgement + Reliability + Keeping_promises + Loss_of_interest + 
                    Friends_versus_money + Funniness + Fake + Criminal_damage + Decision_making + 
                    Elections + Self.criticism + Judgment_calls + Hypochondria + Empathy + Eating_to_survive + 
                    Giving + Compassion_to_animals + Borrowed_stuff + Loneliness + Cheating_in_school + 
                    Health + Changing_the_past + God + Dreams	+ Charity + Number_of_friends + Waiting +
                    New_environment + Mood_swings + Appearence_and_gestures + Socializing + Achievements + 
                    Responding_to_a_serious_letter + Children + Assertiveness + Getting_angry + 
                    Knowing_the_right_people + Public_speaking + Unpopularity + Life_struggles + Happiness_in_life +
                    Energy_levels + Small_big_dogs + Personality + Finding_lost_valuables + Getting_up + Interests_or_hobbies +
                    Parents_advice + Questionnaires_or_polls, data = phobia_personality_data, Hess = TRUE)

summary(model_fit)

summary_table <- coef(summary(model_fit))
pval <- pnorm(abs(summary_table[, "t value"]),lower.tail = FALSE)* 2
summary_table <- cbind(summary_table, "p value" = round(pval,3))
summary_table

write.csv(summary_table,"polr_model_coef_heights_MOSHER.csv", row.names = TRUE)
