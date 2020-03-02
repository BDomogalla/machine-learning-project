library(MASS)

data = read.csv("Data/personality_traits_adjusted_scale_MOSHER.csv", header = TRUE)
View(data)

model_fit <- glm(Gender ~ Daily_events + Prioritising_workload + Writing_notes + Workaholism +
                   Thinking_ahead + Final_judgement + Reliability + Keeping_promises + Loss_of_interest + 
                   Friends_versus_money + Funniness + Fake + Criminal_damage + Decision_making + 
                   Elections + Self_criticism + Judgment_calls + Hypochondria + Empathy + Eating_to_survive + 
                   Giving + Compassion_to_animals + Borrowed_stuff + Loneliness + Cheating_in_school + 
                   Health + Changing_the_past + God + Dreams	+ Charity + Number_of_friends + Waiting +
                   New_environment + Mood_swings + Appearence_and_gestures + Socializing + Achievements + 
                   Responding_to_a_serious_letter + Children + Assertiveness + Getting_angry + 
                   Knowing_the_right_people + Public_speaking + Unpopularity + Life_struggles + Happiness_in_life +
                   Energy_levels + Small_big_dogs + Personality + Finding_lost_valuables + Getting_up + Interests_or_hobbies +
                   Parents_advice + Questionnaires_or_polls, data = data, family="binomial")

summary_table <- coef(summary(model_fit))
summary_table2 <- summary(model_fit)
summary_table2


write.csv(summary_table,"model_coefficients/bi_logic_model_coef_gender_adjscale_MOSHER.csv", row.names = TRUE)
