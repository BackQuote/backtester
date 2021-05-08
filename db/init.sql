TRUNCATE TABLE public.backtest RESTART IDENTITY CASCADE ;
TRUNCATE TABLE public.algorithm RESTART IDENTITY CASCADE ;
TRUNCATE TABLE public.template RESTART IDENTITY CASCADE ;
TRUNCATE TABLE public.simulation RESTART IDENTITY CASCADE ;
TRUNCATE TABLE public.trade RESTART IDENTITY CASCADE ;
TRUNCATE TABLE public.result RESTART IDENTITY CASCADE ;

INSERT INTO public.algorithm (id, name) VALUES (1, 'simple');
INSERT INTO public.template (id, params) VALUES (1, '{"maxLossPerTrade": 0.05, "maxGainPerTrade": 3, "maxDailyLoss": 0.3, "maxDailyGain": 3, "timeBufferEnd": [0, 0, 1], "cash": 15000, "timeBufferStart": [0, 0, 1], "margin": 0.3}');
