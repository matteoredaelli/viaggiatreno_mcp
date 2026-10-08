# Copyright 2026 Matteo Redaelli
# SPDX-License-Identifier: GPL-3.0-or-later

"""Test unitari per la validazione dei modelli Pydantic sui campioni reali."""

from viaggiatreno import (
    DettaglioTratta,
    StationDetail,
    StationSearchResult,
    Statistics,
    TrainBoardItem,
    TrainSearchResult,
    TrainStatus,
    TrattaCanvasItem,
    TrattaSegment,
)

from tests.conftest import load_sample_json


def test_station_search_result_model():
    data = load_sample_json("cercaStazione")
    assert isinstance(data, list)
    item = StationSearchResult.model_validate(data[0])
    assert item.id == "S09314"
    assert item.nomeLungo == "APICE S.ARCANGELO BONITO"
    assert item.label == "Apice"


def test_station_detail_model():
    data = load_sample_json("dettaglioStazione")
    detail = StationDetail.model_validate(data)
    assert detail.codiceStazione == "S01700"
    assert detail.codReg == 1
    assert detail.nomeRegione == "Lombardia"
    assert detail.lat == 45.486347
    assert detail.lon == 9.204528
    assert detail.nomeCitta == "Milano"


def test_elenco_stazioni_model():
    data = load_sample_json("elencoStazioni")
    assert isinstance(data, list)
    stations = [StationDetail.model_validate(item) for item in data]
    assert len(stations) == 345
    assert stations[0].codiceStazione == "S01510"


def test_train_search_result_model():
    data = load_sample_json("cercaNumeroTreno")
    res = TrainSearchResult.model_validate(data)
    assert res.numeroTreno == "9611"
    assert res.codLocOrig == "S00219"
    assert res.descLocOrig == "TORINO PORTA NUOVA"
    assert res.millisDataPartenza == "1791064800000"


def test_train_status_model():
    data = load_sample_json("andamentoTreno")
    status = TrainStatus.model_validate(data)
    assert status.numeroTreno == 9611
    assert status.origine == "TORINO PORTA NUOVA"
    assert status.destinazione == "NAPOLI CENTRALE"
    assert status.ritardo == 7
    assert status.stazioneUltimoRilevamento == "MILANO LAMBRATE"
    assert status.tipoTreno == "PG"
    assert status.statoDescrizione == "Regolare"
    assert status.codiceCliente == 1
    assert status.impresaFerroviaria == "Trenitalia (alta velocità)"
    assert len(status.fermate) == 6
    assert status.fermate[0].stazione == "TORINO PORTA NUOVA"
    assert status.fermate[0].tipoFermata == "P"
    assert status.fermate[-1].stazione == "NAPOLI CENTRALE"
    assert status.fermate[-1].tipoFermata == "A"


def test_partenze_board_model():
    data = load_sample_json("partenze")
    items = [TrainBoardItem.model_validate(x) for x in data]
    assert len(items) == 33
    assert items[0].numeroTreno == 9611
    assert items[0].destinazione == "NAPOLI CENTRALE"
    assert items[0].compNumeroTreno == " FR 9611"
    assert items[0].binarioEffettivoPartenzaDescrizione == "11"


def test_arrivi_board_model():
    data = load_sample_json("arrivi")
    items = [TrainBoardItem.model_validate(x) for x in data]
    assert len(items) == 32
    assert items[0].numeroTreno == 2452
    assert items[0].origine == "PARMA"
    assert items[0].binarioEffettivoArrivoDescrizione == "22"


def test_tratte_canvas_model():
    data = load_sample_json("tratteCanvas")
    items = [TrattaCanvasItem.model_validate(x) for x in data]
    assert len(items) == 6
    assert items[0].first is True
    assert items[0].stazione == "TORINO PORTA NUOVA"
    assert items[-1].last is True
    assert items[-1].stazione == "NAPOLI CENTRALE"


def test_elenco_tratte_model():
    data = load_sample_json("elencoTratte")
    segments = [TrattaSegment.model_validate(x) for x in data]
    assert len(segments) == 135
    assert segments[0].trattaAB == 510
    assert segments[0].trattaBA == 511
    assert segments[0].occupata is True


def test_dettagli_tratta_model():
    data = load_sample_json("dettagliTratta")
    groups = [DettaglioTratta.model_validate(x) for x in data]
    assert len(groups) == 2
    assert len(groups[0].treni) == 5
    assert groups[0].treni[0].numeroTreno == 17807
    assert len(groups[1].treni) == 4


def test_statistics_model():
    data = load_sample_json("statistiche")
    stats = Statistics.model_validate(data)
    assert stats.treniGiorno == 615
    assert stats.treniCircolanti == 579
