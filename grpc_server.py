from concurrent import futures
import logging
import grpc
import MessageService_pb2_grpc
import MessageService_pb2
import transformer


class MessageService():
    def ask(self, request, context):
        # result = MessageService_pb2.MessageResponse(
        #     text="request.text"
        # )
        result = MessageService_pb2.MessageResponse(
            transformer.func(
                text = request.text,
                labels = request.themes
            )
        )
        return result

def serve():
    port = "8080"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    MessageService_pb2_grpc.add_MessageServiceServicer_to_server(MessageService(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
    # print(transformer.func(
    #     "request",
    #     [
    #         "Техническое обслуживание/Неисправность салона/Кухня",
    #         "Техническое обслуживание/Повреждение ВС/Другое",
    #         "Опоздание/неявка на вылет",
    #         "Наземное обслуживание/АЭРОМАР/Отсутствие порций питания/напитков (класс обсл-ния)/Отсутствие БКО",
    #         "Без темы",
    #         "Техническое обслуживание/Неисправность салона/Кресло",
    #         "Техническое обслуживание/Техническое состояние ВС/Неисправность систем ВС"
    #     ]
    # )
    # )

    # def run():
    #     with grpc.insecure_channel('localhost:8086') as channel:
    #         stub = MessageService_pb2_grpc.MessageServiceStub(channel)
    #
    #         response = stub.sendMessage(MessageService_pb2.MessageRequest(text = 'Hi!!!'))
    #
    #     print('answer')
    #     print(response)
    #
    # run()

# [
#                     "Техническое обслуживание/Неисправность салона/Кухня",
#                     "Техническое обслуживание/Повреждение ВС/Другое",
#                     "Опоздание/неявка на вылет",
#                     "Наземное обслуживание/АЭРОМАР/Отсутствие порций питания/напитков (класс обсл-ния)/Отсутствие БКО",
#                     "Без темы",
#                     "Техническое обслуживание/Неисправность салона/Кресло",
#                     "Техническое обслуживание/Техническое состояние ВС/Неисправность систем ВС"
#                 ]