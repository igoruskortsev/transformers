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
            themes = transformer.func(
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

 # python -m grpc_tools.protoc --proto_path=. --python_out=. --pyi_out=. --grpc_python_out=. MessageService.proto
