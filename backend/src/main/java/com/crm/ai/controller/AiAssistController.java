package com.crm.ai.controller;

import com.crm.ai.dto.AiRequestDto;
import com.crm.ai.dto.AiResponseDto;
import com.crm.ai.service.AiAssistService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/ai")
@RequiredArgsConstructor
public class AiAssistController {

    private final AiAssistService aiAssistService;

    @PostMapping("/assist")
    public ResponseEntity<AiResponseDto> assist(@RequestBody AiRequestDto request) {
        return ResponseEntity.ok(aiAssistService.getAssistance(request));
    }
}
